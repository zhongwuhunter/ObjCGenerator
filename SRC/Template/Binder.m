//
//
//  Created by tiger
//
//

#import "${CLASSNAME}.h"
#import "PTFoundation.h"
#import "PTUIkit.h"

@implementation ${CLASSNAME}

- (instancetype)initWithView:(${VIEWNAME} *)aview{
    self = [super init];
    if (self) {
        _view = aview;
    }
    return self;
}



- (void)bindViewModel:(${VIEWMODELNAME} *)aviewModel{
    self.viewModel = aviewModel;
}

- (void)viewWillAppear{
    [self refresh];
}




- (void)refresh{
    [self.view.nm_viewController.view showHUD];
    @weakify(self);
    [[self.viewModel.refreshCommand execute:nil] subscribeNext:^(id x) {
        @strongify(self);
        [self.view.nm_viewController.view hideHUD];
        NSLog(@"refresh %@", x);
    } error:^(NSError *error) {
        @strongify(self);
        [self.view.nm_viewController.view hideHUD];
        NSLog(@"%@", error.domain);
    }];
    
}

















@end



