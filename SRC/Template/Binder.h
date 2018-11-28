//
//
//  Created by tiger
//
//

#import <Foundation/Foundation.h>
#import "${VIEWNAME}.h"
#import "${VIEWMODELNAME}.h"

@interface ${CLASSNAME} : NSObject

@property (nonatomic, strong, readonly) ${VIEWNAME}            *view;
@property (nonatomic, strong) ${VIEWMODELNAME}        *viewModel;

- (instancetype)initWithView:(${VIEWNAME} *)aview;

- (void)bindViewModel:(${VIEWMODELNAME} *)aviewModel;

- (void)viewWillAppear;



@end

